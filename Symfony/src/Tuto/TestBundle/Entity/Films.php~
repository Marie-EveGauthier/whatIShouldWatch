<?php

namespace Tuto\TestBundle\Entity;

use Doctrine\ORM\Mapping as ORM;

/**
 * Films
 *
 * @ORM\Table()
 * @ORM\Entity(repositoryClass="Tuto\TestBundle\Entity\FilmsRepository")
 */
class Films
{
    /**
     * @var integer
     *
     * @ORM\Column(name="id", type="integer")
     * @ORM\Id
     * @ORM\GeneratedValue(strategy="AUTO")
     */
    private $id;

    /**
     * @var string
     *
     * @ORM\Column(name="tire", type="string", length=30)
     */
    private $tire;

    /**
     * @var string
     *
     * @ORM\Column(name="realisateur", type="string", length=40)
     */
    private $realisateur;


    /**
     * Get id
     *
     * @return integer 
     */
    public function getId()
    {
        return $this->id;
    }

    /**
     * Set tire
     *
     * @param string $tire
     * @return Films
     */
    public function setTire($tire)
    {
        $this->tire = $tire;

        return $this;
    }

    /**
     * Get tire
     *
     * @return string 
     */
    public function getTire()
    {
        return $this->tire;
    }

    /**
     * Set realisateur
     *
     * @param string $realisateur
     * @return Films
     */
    public function setRealisateur($realisateur)
    {
        $this->realisateur = $realisateur;

        return $this;
    }

    /**
     * Get realisateur
     *
     * @return string 
     */
    public function getRealisateur()
    {
        return $this->realisateur;
    }
}
