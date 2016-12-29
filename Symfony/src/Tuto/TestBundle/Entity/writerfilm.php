<?php

namespace Tuto\TestBundle\Entity;

use Doctrine\ORM\Mapping as ORM;

/**
 * writerfilm
 *
 * @ORM\Table()
 * @ORM\Entity(repositoryClass="Tuto\TestBundle\Entity\writerfilmRepository")
 */
class writerfilm
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
     * @var integer
     *
     * @ORM\Column(name="id_writer", type="integer")
     */
    private $idWriter;

    /**
     * @var integer
     *
     * @ORM\Column(name="id_film", type="integer")
     */
    private $idFilm;


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
     * Set idWriter
     *
     * @param integer $idWriter
     * @return writerfilm
     */
    public function setIdWriter($idWriter)
    {
        $this->idWriter = $idWriter;

        return $this;
    }

    /**
     * Get idWriter
     *
     * @return integer 
     */
    public function getIdWriter()
    {
        return $this->idWriter;
    }

    /**
     * Set idFilm
     *
     * @param integer $idFilm
     * @return writerfilm
     */
    public function setIdFilm($idFilm)
    {
        $this->idFilm = $idFilm;

        return $this;
    }

    /**
     * Get idFilm
     *
     * @return integer 
     */
    public function getIdFilm()
    {
        return $this->idFilm;
    }
}
