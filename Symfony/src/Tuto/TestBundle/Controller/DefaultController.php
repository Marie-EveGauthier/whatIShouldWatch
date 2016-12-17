<?php

namespace Tuto\TestBundle\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\Controller;

class DefaultController extends Controller
{
    public function indexAction()
    {
        return $this->render('TutoTestBundle:Default:firstview.html.twig');
    }

    public function listeAction()
    {
        $film = $this->getDoctrine()
            ->getRepository('TutoTestBundle:Films')
        ->find(1);

        if($film) {
            return $this->render('TutoTestBundle:Default:index.html.twig', array(
                'film' => $film->getTire(), 'realisator' => $film-> getRealisateur()
            ));
        } else {
            return $this->render('TutoTestBundle:Default:index.html.twig',array(
                'film' => '',
                'realisator' => ''
            ));
        }

    }



}
